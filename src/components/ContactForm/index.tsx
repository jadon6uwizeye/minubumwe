import React, { useState, useEffect, FormEvent } from "react";
import { Row, Col } from "antd";
import { withTranslation } from "react-i18next";
import { Slide, Zoom } from "react-awesome-reveal";
import { ContactProps, ValidationTypeProps } from "./types";
import { useForm } from "../../common/utils/useForm";
import validate from "../../common/utils/validationRules";
import { Button } from "../../common/Button";
import Block from "../Block";
import Input from "../../common/Input";
import TextArea from "../../common/TextArea";
import { ContactContainer, FormGroup, Span, ButtonContainer } from "./styles";
import axios from "axios";
import { get } from "http";

interface Sector {
  id: number;
  sector: string;
}

const Contact = ({ title, content, id, t }: ContactProps) => {
  const [sectors, setSectors] = useState<Sector[]>([]);
  const [genocideSurvivorCertificate, setGenocideSurvivorCertificate] = useState<File | null>(null);
  const [deprivedCertificate, setDeprivedCertificate] = useState<File | null>(null);

  const { values, errors, handleChange, handleSubmit } = useForm(validate) as any;

  const ValidationType = ({ type }: ValidationTypeProps) => {
    const ErrorMessage = errors[type];
    return (
      <Zoom direction="left">
        <Span errors={errors[type]}>{ErrorMessage}</Span>
      </Zoom>
    );
  };

  useEffect(() => {
    // Fetch the list of sectors from the API
    axios
      .get("http://127.0.0.1:8000/api/services/sector")
      .then((response) => {
        setSectors(response.data);
      })
      .catch((error) => {
        console.error("Error fetching sectors:", error);
      });
  }, []);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>, fileType: string) => {
    const file = e.target.files?.[0] || null;
    if (fileType === "genocide_survivor_certificate") {
      setGenocideSurvivorCertificate(file);
    } else if (fileType === "deprived_certificate") {
      setDeprivedCertificate(file);
    }
  };

  

  const submitForm = async (e: FormEvent) => {
    e.preventDefault();
    if (!localStorage.getItem("token")){
      alert("Please login to continue.");
      window.location.href = "/login";
      return;
    }
    if (
      !genocideSurvivorCertificate ||
      !values.social_status_class ||
      !deprivedCertificate ||
      !values.sector ||
      !values.message
    ) {
      alert("Please fill in all required fields.");
      return;
    }
    
    // Prepare the data to be sent to the backend API
    const requestData = {
      genocide_survivor_certificate: genocideSurvivorCertificate,
      social_status_class: values.social_status_class,
      deprived_certificate: deprivedCertificate,
      sector: values.sector,
      message: values.message,
    };

    const formadata = new FormData();
    genocideSurvivorCertificate&&formadata.append("genocide_survivor_certificate",genocideSurvivorCertificate)
    deprivedCertificate&&formadata.append("deprived_certificate",deprivedCertificate)
    formadata.append("social_status_class",values.social_status_class)
    formadata.append("sector",values.sector)
    formadata.append("message",values.message)
    try {
      // print token from local storage
      const response = await axios.post(
        "http://127.0.0.1:8000/api/services/request",
        formadata,
        {
          headers: {
            "Content-Type": "multipart/form-data",
            // add bearer token to the request
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        }
      );

      console.log(response.status, 'response');
      if (response.status === 201) {
        // Successful request, handle accordingly
        alert("Request sent successfully! We will get back to you soon");
        window.location.href = "";
      } 
      else if (response.status == 403) {
        // alert("Please login to continue."); and on ok redirect to login page
        console.log("Please login to continue.");
        alert("Please login to continue.");
      }
      else {
        // Handle request error here, e.g., display an error message
        console.error("Request failed.");
      }
    } 
    // Catch 403 error
    catch (error) {
      if(error == "Error: Request failed with status code 401"){
        alert("Please login to continue.");
        return window.location.href = "/login";
      }
      alert(error)
      console.error("Request error:", error);
    }
  };

  return (
    <ContactContainer id={id}>
      <Row justify="space-between" align="middle">
        <Col lg={12} md={11} sm={24} xs={24}>
          <Slide direction="left">
            <Block title={title} content={content} />
          </Slide>
        </Col>
        <Col lg={12} md={12} sm={24} xs={24}>
          <Slide direction="right">
            <FormGroup autoComplete="off">
              <Col span={24}>
                <Input
                  type="file"
                  name="genocide_survivor_certificate"
                  placeholder="Genocide Survivor Certificate"
                  onChange={(e: any) => handleFileChange(e, "genocide_survivor_certificate")}
                />
                <ValidationType type="genocide_survivor_certificate" />
              </Col>
              <Col span={24}>
                <Input
                  type="text"
                  name="social_status_class"
                  placeholder="Social Status Class"
                  value={values.social_status_class || ""}
                  onChange={handleChange}
                />
                <ValidationType type="social_status_class" />
              </Col>
              <Col span={24}>
                <Input
                  type="file"
                  name="deprived_certificate"
                  placeholder="Deprived Certificate"
                  onChange={(e: any) => handleFileChange(e, "deprived_certificate")}
                />
                <ValidationType type="deprived_certificate" />
              </Col>
              <Col span={24}>
                <select
                  name="sector"
                  value={values.sector || ""}
                  onChange={handleChange}
                >
                  <option value="">Select Sector</option>
                  {sectors.map((sector) => (
                    <option key={sector.id} value={sector.id}>
                      {sector.sector}
                    </option>
                  ))}
                </select>
                <ValidationType type="sector" />
              </Col>
              <Col span={24}>
                <TextArea
                  placeholder="Your Message"
                  // make it required
                  value={values.message}
                  name="message"
                  onChange={handleChange}
                />
                <ValidationType type="message" />
              </Col>
              <ButtonContainer>
                <Button onClick={(e: any) =>submitForm(e)}>Submit</Button>
              </ButtonContainer>
            </FormGroup>
          </Slide>
        </Col>
      </Row>
    </ContactContainer>
  );
};

export default withTranslation()(Contact);
